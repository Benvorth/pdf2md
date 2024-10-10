# pdf2md

Convert a pdf (given by url) to markdown format

## Backgorund

This project wraps the `pymupdf4llm` lib in a RESTful microservice.

## Request

````
GET http://localhost:8081/pdf2md/api/common/alive/


POST http://localhost:8081/pdf2md/api/convert
body:
{
    "pdf_url": "https://www.somepage.com/docs/the_file.pdf"
}
````


## License

GNU AFFERO GPL 3.0, inherit from `pymupdf4llm`
