from typing import Any
from wtforms.fields import simple

class Foo(object):

    def __init__(self,*args,**kwargs) :
        super().__init__()  
        pass
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass    
    def __str__(self) -> str:
        pass
    def __new__(cls) -> Self:
        pass


