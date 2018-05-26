import functions


class App:
    map = {
        1: 'add_matrix',
        2: 'subtract_matrix',
        3: 'get_determinant',
        4: 'transpose',
        5: 'multiply_matrix'
    }

    def run(self):
        print('Choose your operation from list (1-5):\n')
        print('1: Add matrix B to matrix A\n')
        print('2: Subtract matrix B from matrix A\n')
        print('3: Get matrix A determinant\n')
        print('4: Transpose matrix A\n')
        print('5: Multiply matrix A on number\n')

        choice = int(input())

        try:
            getattr(functions, self.map[choice])()
        except KeyError:
            print('Incorrect option have been selected! \n')
            self.run()


App().run()
