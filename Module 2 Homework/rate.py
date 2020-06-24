if __name__ == '__main__':
    print('This program calculates gross pay based on hours worked and hourly pay rate.')
    hours = input('Enter hours worked: ')
    rate = input('Enter hourly rate: ')
    gross_pay = int(hours) * int(rate)
    print(f'Gross pay = {gross_pay}')