from app import app
from flask import jsonify, request

books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    """
    Get a list of all books
    ---
    responses:
        200:
            description: A list of books
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            description: The book ID
                        title:
                            type: string
                            description: The book title
                        author:
                            type: string
                            description: The book author
    """
    return jsonify(books)

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Get a book by ID
    ---
    parameters:
    - name: book_id
      in: path
      type: integer
      required: true
      description: The ID of the book
    responses:
        200:
            description: A single book
            schema:
                type: object
                properties:
                    id:
                        type: integer
                        description: The book ID
                    title:
                        type: string
                        description: The book title
                    author:
                        type: string
                        description: The book author
        404:
            description: Book not found
    """
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify(book) if book else ('', 404)

@app.route('/api/books', methods=['POST'])
def add_book():
    """
    Add a new book
    ---
    parameters:
    - name: book
      in: body
      required: true
      schema:
          type: object
          properties:
              id:
                  type: integer
              title:
                  type: string
              author:
                  type: string
    responses:
        201:
            description: The created book
            schema:
                type: object
                properties:
                    id:
                        type: integer
                    title:
                        type: string
                    author:
                        type: string
    """
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update an existing book by ID
    ---
    parameters:
    - name: book_id
      in: path
      type: integer
      required: true
      description: The ID of the book
    - name: book
      in: body
      required: true
      schema:
          type: object
          properties:
              title:
                  type: string
              author:
                  type: string
    responses:
        200:
            description: The updated book
            schema:
                type: object
                properties:
                    id:
                        type: integer
                    title:
                        type: string
                    author:
                        type: string
        404:
            description: Book not found
    """
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return ('', 404)

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Delete a book by ID
    ---
    parameters:
    - name: book_id
      in: path
      type: integer
      required: true
      description: The ID of the book
    responses:
        204:
            description: No content, book deleted
        404:
            description: Book not found
    """
    global books
    books = [book for book in books if book['id'] != book_id]
    return ('', 204)
