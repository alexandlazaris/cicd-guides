import pytest
import os.path

htmlFileName = "index.html"
reportsDir = "./test-reports"


def test_canCreateHtmlFile(): # tweak assertion to be on html feature rather than os.exists
    html = open(htmlFileName, 'a')
    html.truncate(0)
    html.close()
    assert (os.path.exists(htmlFileName) is True)
    os.remove(htmlFileName)

def test_htmlDoesNotExist():
    assert (os.path.exists(htmlFileName) is False)

# def test_reportsDirDoesNotExist():
    # assert (os.path.isdir(reportsDir) is False)