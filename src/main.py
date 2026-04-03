import uuid

from task import Task


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    t = Task(uuid.uuid4(),"dgfgjhbknjlm",1)
    print(t.description)
    print(t.is_ready)
    try:
        t.status = 'ready1'
    except Exception as e:
        print(e)
    t.status = 'ready'
    print(t.is_ready)

if __name__ == "__main__":
    main()
