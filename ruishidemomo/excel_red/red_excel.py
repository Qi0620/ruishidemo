import openpyxl

from ruishidemomo.api_keyword.inter_params import InterParams


class RedExcel:

    def read_excle(self):
        # wb = openpyxl.load_workbook("../data/test_ruis.xlsx")
        wb = openpyxl.load_workbook("./ruishidemomo/data/test_ruis.xlsx")
        sheet = wb["info"]

        models = []
        for s_name in sheet.values:
            print(s_name,"sname")
            # if s_name[16] == 1:
            if type(s_name[18]) is int:
                ip = InterParams()
                ip.url = s_name[0]
                ip.desc = s_name[1]
                ip.method = s_name[2]
                ip.headers = s_name[3]
                ip.data = s_name[4]
                ip.assert_data = s_name[5]
                ip.assert_options = s_name[6]
                ip.assert_values = s_name[7]
                ip.extract = s_name[8]
                ip.is_need = s_name[9]
                ip.return_data = s_name[10]
                ip.par_type = s_name[11]
                ip.story = s_name[12]
                ip.feature = s_name[13]
                ip.backup = s_name[14]
                ip.level = s_name[15]
                ip.is_go = s_name[16]
                #是否执行通过，这个不需要添加进来[17]
                ip.idd = s_name[18]
                print(ip.url, ip.desc, ip.method, ip.headers, ip.data,ip.idd)
                models.append(ip)
        print(models)
        return models


if __name__ == '__main__':
    rd = RedExcel()
    rd.read_excle()
