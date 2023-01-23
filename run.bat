set root=D:\DFiles\Programs\PyCharmProjects\hybridframework-python-selenium
cd /D %root%
pytest -s -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./Reports/report_edge.html testCases/ --browser edge

rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
pause