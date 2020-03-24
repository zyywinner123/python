from appium import webdriver
import time
import xlrd
import os


def is_content_Appeared(content):
    try:
        driver.find_element_by_name(content)
        status=True
    except:
        status = False
    return status
def click_control(name1,name):
    if name1=="ida":
        time.sleep(3)
        driver.find_element_by_accessibility_id(name).click()
    if name1=="name":
        time.sleep(3)
        driver.find_element_by_name(name).click()
    if name1=="id":
        time.sleep(3)
        driver.find_element_by_id(name).click()
    return
 # os.system("adb connect 46735145")
book=xlrd.open_workbook("模板1.xls")
sheet_name=book.sheet_names()[0]
sheet = book.sheet_by_name(sheet_name)
nrows = sheet.nrows
desired_caps = {'platformName': 'Android',
                'deviceName': '46735145',
                'platformVersion': '4.4.2',#将要测试app的安装包放到自己电脑上执行安装或启动，如果不是从安装开始，则不是必填项，可以由下面红色的两句直接启动
                'appPackage': 'com.tencent.mm', #红色部分如何获取下面讲解
                'appActivity': 'com.tencent.mm.ui.LauncherUI',
                'unicodeKeyboard': True, #此两行是为了解决字符输入不正确的问题
                'resetKeyboard': True, #运行完成后重置软键盘的状态
                # 'autoWebview':True,
                'recreateChromeDriverSessions':True,
                'automationName':'Appium'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
w=1
for x in range(1,5):
    try:
        time.sleep(5)
        click_control("ida", "更多功能按钮")
        click_control("name", "添加朋友")
        click_control("name", "微信号/QQ号/手机号")
        for i in range(w,nrows):
            row = sheet.row_values(i)
            click_control("id","com.tencent.mm:id/hz")#点击搜索框
            time.sleep(30)
            print(row)
            driver.find_element_by_id("com.tencent.mm:id/hz").send_keys(str(int(row[2])))#输入电话号码
            click_control("name","搜索:"+str(int(row[2])))
            if is_content_Appeared("该用户不存在")==True:
                driver.find_element_by_id("com.tencent.mm:id/hx").clear()
                print(int(row[2]),"用户不存在")
            elif is_content_Appeared("操作过于频繁，请稍后再试"):
                print(int(row[2]),"操作过于频繁，请稍后再试")
                driver.quit()
                break
            elif is_content_Appeared("发消息")==True:
                print(int(row[2]),"该用户已经添加为好友")
                click_control("name","返回")
            elif is_content_Appeared("添加到通讯录")==True:
                if is_content_Appeared("设置备注和标签")==True:
                    click_control("name","设置备注和标签")
                    click_control("name","添加标签对联系人进行分类" )
                    driver.find_element_by_name("添加标签").send_keys(row[3]) # 获取标签名
                    click_control("name","保存")
                    click_control("ida", "返回")
                    click_control("name","添加到通讯录")
                    click_control("id","com.tencent.mm:id/d4l")
                    driver.find_element_by_id("com.tencent.mm:id/d4l").clear()  # 清除备注名
                    driver.find_element_by_id("com.tencent.mm:id/d4l").send_keys(row[0]+ "(" + row[1]+ ")")  # 输入被备注名
                    click_control("name","发送")
                    print("成功发送验证消息！")
                    click_control("name","返回")
                elif is_content_Appeared("设置备注和标签")==False:
                    click_control("name", "添加到通讯录")
                    click_control("id", "com.tencent.mm:id/d4l")
                    driver.find_element_by_id("com.tencent.mm:id/d4l").clear()  # 清除备注名
                    driver.find_element_by_id("com.tencent.mm:id/d4l").send_keys(row[0]+ "(" + row[1]+ ")")  # 输入被备注名
                    click_control("name", "发送")
                    print("成功发送验证消息！")
                    click_control("name", "返回")
            else:
                driver.save_screenshot("app" + str(i) + ".png")
                print("其他情况")
            w=w+1
    except BaseException as e:
        print(e)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)