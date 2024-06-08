"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
"""
"Test message" будет выведено только 1 раз внутри функции data_transmitter
print(transmit_to_space("Test message")) выведет None поскольку во всех вложенных функциях нет return
"""