# 1번

class NegativeValueError(ValueError):
    def __init__(self, message="입력 값이 음수 입니다"):
        super().__init__(message)

def validate_positive(value):
    if value < 0:
        raise NegativeValueError()
    return value


#2번
class Fibonaccilterator:
    def __init__(self, n):
        """
        Fibonaccilterator 클래스의 생성자.

        Args:
            n (int): 생성할 피보나치 수의 개수.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("n은 0 이상의 정수여야 합니다.")
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        """
        클래스 객체를 반복 가능하게 만드는 메서드.
        """
        return self

    def __next__(self):
        """
        다음 피보나치 수를 반환하는 메서드.
        """
        if self.count < self.n:
            if self.count == 0:
                result = self.a
            elif self.count == 1:
                result = self.b
            else:
                result = self.a + self.b
                self.a, self.b = self.b, result
            self.count += 1
            return result
        else:
            raise StopIteration


#3번
def partial(func, *args, **kwargs):
    # partial 함수는 내부에 클로저를 이용하여 이미 전달된 인수를 고정시킵니다.
    def wrapper(*more_args, **more_kwargs):
        # 기존의 키워드 인수와 추가로 받은 키워드 인수를 병합합니다.
        new_kwargs = kwargs.copy()
        new_kwargs.update(more_kwargs)
        # 기존의 인수와 추가 인수를 결합하여 func를 호출합니다.
        return func(*args, *more_args, **new_kwargs)
    return wrapper