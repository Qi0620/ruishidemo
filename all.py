import os

import pytest

if __name__ == '__main__':
    # pytest.main(['--alluredir','./ruishidemomo/result/','--clean-alluredir'])
    # 使用--reruns ，错误用例重新执行几次
    # 使用  --reruns-delay  ，下次执行需等待几秒
    # "--reruns",'2','--reruns-delay','2',
    # 生成测试报告
    # '--html=../htmlreport/report.html','do_excel_interface_allure.py'
    # pytest.main()
    # os.system('allure generate ./ruishidemomo/result/ -o ./ruishidemomo/report --clean')
    # os.system('allure serve result')

    pytest.main(['--alluredir','./ruishidemomo/result/','--clean-alluredir'])
    os.system('allure generate ./ruishidemomo/result/ -o ./ruishidemomo/report --clean')
