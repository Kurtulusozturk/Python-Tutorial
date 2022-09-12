class Book:
    

    def __init__(self,name,page):
        self.name=name
        self.page=page
    
    
    @classmethod
    def from_list(cls,data):
        books=[]
        for book in data:
            books.append(cls(name=book['name'],page=book['page']))
            return books


data=[
    {
        "name":"a1",
        "page":60
    },
    {
        "name":"a2",
        "page":79
    },
    {
        "name":"a3",
        "page":90
    }
]

books=Book.from_list(data=data)
print(books[0].name)

# book= Book('kitap adi',20)
# book2=Book('asdas',20)