import time ,sys,unittest
sys.path.append(r'./test_case')
from HTMLTestRunner import HTMLTestRunner

test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="*_case.py")
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "./test_report/" + now + "result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="《pc音视频管理后台》测试用例统计报告",
        description="环境：Windows7  浏览器：chrome"
    )
    runner.run(discover)
    fp.close()