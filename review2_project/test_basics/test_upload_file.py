from pages.upload_page import UploadPage

def test_upload_file(page):
    upload_page=UploadPage(page)
    # GO TO UPLOAD PAGE
    upload_page.access_page()
    # SELECT FILE
    file_path="/Users/giangpham/PycharmProjects/download_files/downloadsm.jpg"
    sel=upload_page.select_file()
    sel.set_input_files(file_path)
    # SUBMIT FILE
    upload_page.submit_file()
    # VERIFY UPLOADED FILE
    name=upload_page.verify_uploaded_file()
    assert name in file_path

