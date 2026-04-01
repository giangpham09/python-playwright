from pages.download_page import DownloadPage

def test_download_file(page):
    download_page=DownloadPage(page)
    # GO TO DOWNLOAD PAGE
    download_page.access_page()
    # DOWNLOAD EVENTS
    with page.expect_download() as download_jpg:
        download_page.download_JPG()
    download1=download_jpg.value
    # SAVE DOWNLOAD FILES
    download1.save_as("/Users/giangpham/PycharmProjects/download_files/download" + download1.suggested_filename)
    # VERIFY AFTER DOWNLOADING
    assert download1.failure() is None


