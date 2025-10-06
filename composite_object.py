# exercise: design a composite object
# by: Malini Fielhauer & Leonie Theiser


# task 1
document = {
    "title" : "The Enigma Mind",
    "author" : {
        "name": "Dr. Elanor Hughes",
        "birth date" : "September 12th",
        "nationality" : "british",
        "contact_information_author" : {
            "email" : "eleanor.hughes@oxfordpress.co.uk",
            "phone" : "+447700321456" } ,
        "awards" : ["Royal Society Science Writing Price 2017", "British Book Award of Non- Fiction 2021"]

    } ,
    "summary" : " A biographical exploration of Alan Turings life, his groundbreaking work in mathematics and computing and the lasting legacy of his ideas that shaped the modern digital world.",
"page count" : 412 ,
"printing_cost" : "8.90 GBP" ,
"publisher" : {
    "name" : "Oxford Press" ,
    "address" : {
        "street" : "27 Broad Street" ,
        "city" : "Oxford" ,
        "ZIP" : "OX1 3BQ"
    } ,
    "contact_information_publisher" : {
            "email" : "info@oxfordpress.co.uk",
            "phone" : "+441865276000" }
}
        }


# task 2
print(document["summary"])
print(document["author"]["name"])
print(document["publisher"]["address"]["street"])


# task 3
document["publisher"]["contact_information_publisher"]["phone"] = "+441865277000"
print(document["publisher"]["contact_information_publisher"]["phone"])

document["author"]["awards"].append("Pandaward 2025")
print(document["author"]["awards"])



