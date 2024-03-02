import streamlit as st

def main():
    st.title("Image Gallery")

    # Define image data
    image_data = [
        {"image": "image_url1.jpg", "description": "Description 1", "web_link": "https://example.com/1"},
        {"image": "image_url2.jpg", "description": "Description 2", "web_link": "https://example.com/2"},
        {"image": "image_url3.jpg", "description": "Description 3", "web_link": "https://example.com/3"},
    ]

    # Display image gallery
    for item in image_data:
        st.image(item["image"], caption=item["description"], use_column_width=True)
        st.write("Description:", item["description"])
        st.write("Web Link:", item["web_link"])

if __name__ == "__main__":
    main()
