from models.Book import Book


def get_book_with_id(book: Book, books_list):
    book.id = 1 if len(books_list) == 0 else books_list[-1].id + 1
    return book