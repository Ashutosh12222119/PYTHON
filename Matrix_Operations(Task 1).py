import numpy as np

def get_matrix(matrix_name):
    rows, cols = map(int, input(f"\nEnter the number of Rows and Columns (Space-Seperated) for {matrix_name}: ").split())
    # cols = int(input(f"Enter the number of columns for {matrix_name}: "))
    print(f"Enter the elements of {matrix_name} row-wise (space-separated) : ")
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(float, input().split())))
    return np.array(matrix)

def display_menu():
    print("\nMatrix Operations Tool")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an Operation You Want To Perform (1-6): ")

        if choice == '1':  # Addition of Matrix
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape == B.shape:
                print("Result:\n", A + B)
            else:
                print("Error: Matrices Must Have The Same Dimensions for Addition.")

        elif choice == '2':  # Subtraction of Matrix
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape == B.shape:
                print("Result:\n", A - B)
            else:
                print("Error: Matrices Must Have The Same Dimensions for Subtraction.")

        elif choice == '3':  # Multiplication of Matrix
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                print("Result:\n", np.dot(A, B))
            else:
                print("Error: Number of columns of A must match number of rows of B.")

        elif choice == '4':  # Transpose of Matrix
            A = get_matrix("Matrix A")
            print("Transpose:\n", A.T)

        elif choice == '5':  # Determinant of Matrix
            A = get_matrix("Matrix A")
            if A.shape[0] == A.shape[1]:
                print("Determinant:", np.linalg.det(A))
            else:
                print("Error: Determinant can only be calculated for square matrices.")

        elif choice == '6':  # Exit
            print("Exiting The Program. Have a Nice Day Mam/Sir !\n")
            break

        else:
            print("Invalid Choice. Please Select a Valid Option.\n")

if __name__ == "__main__":
    main()
