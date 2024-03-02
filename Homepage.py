import streamlit as st

class Book:
    def __init__(self, image, description, web_link):
        self.image = image
        self.description = description
        self.web_link = web_link

class BookClass:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

def main():
    st.title("My Books")

    # Define book classes
    book_classes = {"Python": BookClass("Python"),  "Machine Learning": BookClass("Machine Learning"), "Deep Learning": BookClass("Deep Learning"), "Artificial Intelligence": BookClass("Artificial Intelligence"), "Data Science": BookClass("Data Science"), "Excel and PowerBI": BookClass("Excel and PowerBI")}

    # Add books to their respective classes
    book_classes["Python"].add_book(Book("PY1.JPG", "Learning Professional Python", "https://www.linkedin.com/posts/masrulmollah_learning-professional-python-activity-7169699011485007872-nJZ3?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY2.JPG", "Python for Data Science", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY3.JPG", "Python Guide", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY4.JPG", "Python For Excel", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY5.JPG", "Master Python in 15 Days", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY6.JPG", "Python Numpy", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY7.JPG", "Python By Examples", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY8.JPG", "Python Tricks", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY9.JPG", "Real Python", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY10.JPG", "Think Python", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY11.JPG", "Python Debugging for AI ML and Cloud Computing", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))
    book_classes["Python"].add_book(Book("PY12.JPG", "Python Tutorial (Codes)", "https://www.linkedin.com/posts/masrulmollah_python-for-data-science-activity-7169700105065889792-Humx?utm_source=share&utm_medium=member_desktop"))


    book_classes["Machine Learning"].add_book(Book("ML1.JPG", "Python Machine Learning Projects", "https://www.example.com"))
    book_classes["Machine Learning"].add_book(Book("ML2.JPG", "Python Machine Learning", "https://www.example.com"))
    book_classes["Machine Learning"].add_book(Book("ML3.JPG", "Python for Statistics and Machine Learning", "https://www.example.com"))
    book_classes["Machine Learning"].add_book(Book("ML4.JPG", "Machine Learning A to Z ++", "https://www.example.com"))
    book_classes["Machine Learning"].add_book(Book("ML5.JPG", "Machine Learning The Archive", "https://www.example.com"))
    book_classes["Machine Learning"].add_book(Book("ML6.JPG", "Amazon Machine Learning", "https://www.example.com"))
    book_classes["Machine Learning"].add_book(Book("ML7.JPG", "Lecture Note on Machine Learning", "https://www.example.com"))

    book_classes["Deep Learning"].add_book(Book("DL1.JPG", "A Visual Introduction to Deep Learning", "https://www.example.com"))
    book_classes["Deep Learning"].add_book(Book("DL1.JPG", "A Visual Introduction to Deep Learning", "https://www.example.com"))

    book_classes["Artificial Intelligence"].add_book(Book("AI1.JPG", "Applied Generative AI for the Beginners", "https://www.example.com"))
    book_classes["Artificial Intelligence"].add_book(Book("AI2.JPG", "How to Learn AI the Beginners Guide", "https://www.example.com"))
    book_classes["Artificial Intelligence"].add_book(Book("AI3.JPG", "AI for Data Science", "https://www.example.com"))
    book_classes["Artificial Intelligence"].add_book(Book("AI4.JPG", "Lecture Notes on AI", "https://www.example.com"))
    book_classes["Artificial Intelligence"].add_book(Book("AI5.JPG", "Python Code for AI", "https://www.example.com"))

    book_classes["Data Science"].add_book(Book("DS1.JPG", "Data Science", "https://www.example.com"))
    book_classes["Data Science"].add_book(Book("DS2.JPG", "The Art of Data Science", "https://www.example.com"))
    book_classes["Data Science"].add_book(Book("DS3.JPG", "Data Visualization with Pandas", "https://www.example.com"))

    book_classes["Excel and PowerBI"].add_book(Book("XPBI1.JPG", "PowerBI Magic in 30 days", "https://www.linkedin.com/posts/masrulmollah_learn-powerbi-magic-on-30-days-activity-7169701048155131904-yqxu?utm_source=share&utm_medium=member_desktop"))
    book_classes["Excel and PowerBI"].add_book(Book("XPBI2.JPG", "Excel Formulas", "https://www.linkedin.com/posts/masrulmollah_excel-formulas-activity-7169703344960122880-KDgq?utm_source=share&utm_medium=member_desktop"))
    book_classes["Excel and PowerBI"].add_book(Book("XPBI3.JPG", "Excel Formulas Bible", "https://www.linkedin.com/posts/masrulmollah_excel-formulas-bible-activity-7169702351014912001-isJ9?utm_source=share&utm_medium=member_desktop"))


    # Create sidebar for selecting book classes and descriptions
    selected_class_name = st.sidebar.selectbox("Select Book Class", list(book_classes.keys()))

    # Display book descriptions for the selected class in the sidebar
    st.sidebar.subheader("Book Descriptions")
    selected_class = book_classes[selected_class_name]
    selected_description = st.sidebar.radio("", [book.description for book in selected_class.books])

    # Find the selected book
    selected_book = None
    for book in selected_class.books:
        if book.description == selected_description:
            selected_book = book
            break

    # Display the selected book at the top of the webpage
    if selected_book:
        st.header("Selected Book")
        col1, col2 = st.columns([1, 1.5])
        col1.image(selected_book.image, caption=selected_book.description, width=265)
        with col2:
            st.write("Description:", selected_book.description)
            st.write("Web Link:", selected_book.web_link)
        st.write("----")


    # Display all books of the selected class at the top
    st.header(selected_class.name)
    for book in selected_class.books:
        col1, col2 = st.columns([1, 1.5])
        col1.image(book.image, caption=book.description, width=265)
        with col2:
            st.write("Description:", book.description)
            st.write("Web Link:", book.web_link)
        st.write("----")


    # Display books from other classes
    for class_name, book_class in book_classes.items():
        if class_name != selected_class_name:
            st.header(book_class.name)
            for book in book_class.books:
                col1, col2 = st.columns([1, 1.5])
                col1.image(book.image, caption=book.description, width=265)
                with col2:
                    st.write("Description:", book.description)
                    st.write("Web Link:", book.web_link)
                st.write("----")

if __name__ == "__main__":
    main()
