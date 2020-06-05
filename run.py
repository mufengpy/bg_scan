import time
import threading

from ui import *
from helper import get_ui_args, scan, CheckUrl
import tools

column_names = ['地址', 'HTTP响应']
dic_files = ['DIR', 'PHP', 'ASP', 'MDB', 'JSP', 'ASPX']
list_code = ['2XX', '3XX', '4XX']
file_line_dict = None  # 各字典的大小
need_dic_line_nums = 0  # 加载的字典总大小


class MyNotebook(MyFrame1):

    def initUI(self):
        '初始化界面参数'
        self.initUIGrit()  # 初始化表格标题
        self.initUISetArgs()  # 初始化各文件行数

    def initUISetArgs(self):
        '初始化配置参数'
        global file_line_dict
        file_line_dict = get_ui_args()
        # print(file_line_dict)
        # {'ASP.txt': 1853, 'ASPX.txt': 821, 'DIR.txt': 1152, 'JSP.txt': 630, 'MDB.txt': 418, 'PHP.txt': 1065}
        # print(lines)
        self.m_checkBox1.SetLabel('DIR:{}'.format(file_line_dict['DIR.txt']))
        self.m_checkBox12.SetLabel('PHP:{}'.format(file_line_dict['PHP.txt']))
        self.m_checkBox11.SetLabel('ASP:{}'.format(file_line_dict['ASP.txt']))
        self.m_checkBox111.SetLabel('MDB:{}'.format(file_line_dict['ASP.txt']))
        self.m_checkBox112.SetLabel('JSP:{}'.format(file_line_dict['JSP.txt']))
        self.m_checkBox2.SetLabel('ASPX:{}'.format(file_line_dict['ASPX.txt']))

    def getUIArgs(self):
        val_m_textCtrl2 = self.m_textCtrl2.GetValue()
        val_m_choice1 = self.m_choice1.GetStringSelection()
        val_m_choice11 = self.m_choice11.GetStringSelection()
        is_selected_m_checkBox1 = self.m_checkBox1.Get3StateValue()
        is_selected_m_checkBox12 = self.m_checkBox12.Get3StateValue()
        is_selected_m_checkBox11 = self.m_checkBox11.Get3StateValue()
        is_selected_m_checkBox111 = self.m_checkBox111.Get3StateValue()
        is_selected_m_checkBox112 = self.m_checkBox112.Get3StateValue()
        is_selected_m_checkBox2 = self.m_checkBox2.Get3StateValue()
        is_selected_m_checkBox3 = self.m_checkBox3.Get3StateValue()
        is_selected_m_checkBox31 = self.m_checkBox31.Get3StateValue()
        is_selected_m_checkBox113 = self.m_checkBox113.Get3StateValue()

        # 每行作为一组
        value_args = [val_m_textCtrl2, [val_m_choice1, val_m_choice11],
                      [is_selected_m_checkBox1, is_selected_m_checkBox12,
                       is_selected_m_checkBox11], [is_selected_m_checkBox111, is_selected_m_checkBox112,
                                                   is_selected_m_checkBox2],
                      [is_selected_m_checkBox3, is_selected_m_checkBox31, is_selected_m_checkBox113]]

        # ['2', '3', 1, 1, 0, 0, 0, 0, 1, 1, 1]
        return value_args

    def initUIGrit(self):
        '初始化表格'
        for col in range(len(column_names)):
            self.m_grid1.SetColLabelValue(col, column_names[col])

    def OnstartScan(self, event):

        def inner():
            # 清空数据栏
            self.m_grid1.ClearGrid()

            args = self.getUIArgs()

            input_url = args[0]
            timeout = int(args[1][1])
            need_dic = args[2] + args[3]
            need_status_code = args[4]

            file_line_tuple = tuple(file_line_dict.values())
            need_dic_line_nums = sum([file_line_tuple[index] for index, item in enumerate(need_dic) if item == 1])
            print(need_dic_line_nums)

            # 加载字典
            files = ['conf/' + item[1] + '.txt' for item in zip(need_dic, dic_files) if item[0]]
            # print(files)

            need_status_code = [item[1] for item in zip(need_status_code, list_code) if item[0]]

            # 检测URL是否合法,合法则返回一个有效url
            domain_url = CheckUrl(input_url)
            if not domain_url:
                print('url为空')
                return

            print(domain_url)

            for fname in files:
                for item in tools.file_text(fname):
                    # time.sleep(0.5)
                    url = domain_url + item[1]
                    # 开始扫描
                    thread_obj = threading.Thread(target=scan,
                                                  args=(self, url, need_status_code, need_dic_line_nums, timeout))
                    thread_obj.start()
                    # 延迟
                    time.sleep(0.2)

        # 事件触发方法，会导致BUG:界面无法响应.可用多线程解决
        thread_obj = threading.Thread(target=inner, args=(), name='OnstartScan')
        thread_obj.start()

    def OnstopScan(self, event):
        def inner():
            print('OnstopScan')
            print(threading.enumerate())
            for item in threading.enumerate():
                if item.getName() == 'OnstartScan':
                    tools.stop_thread(item)

        # 事件触发方法，会导致BUG:界面无法响应.可用多线程解决
        thread_obj = threading.Thread(target=inner, args=(), name='OnstopScan')
        thread_obj.start()


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyNotebook(parent=None)
        frame.Show()
        return True

    def column_names(self):
        return


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
