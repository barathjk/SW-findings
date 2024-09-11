import json
import glob
import pandas as pd
import os

global cs_teamscale_finding, arch_teamscale_finding, qac_teamscale_finding, modeladvisor_finding, file, json_file, file_path, f, data_file, each_data, each_findings_in_each_data
global folder_path, finding_option
finding_option = "codesonar, architecture, qac, modeladvisor"


folder_path = 'CCU01_BEV21'
current_dir = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(current_dir, folder_path)
def cs_teamscale():
    global folder_path
    cs_teamscale_finding = {
        "PrjName": [],
        "CPSName": [],
        "SWCName": [],
        "FilePath": [],
        "Warning": [],
        "findingTypeId": [],
        "uniqueId": [],
    }
    for file in os.listdir(folder_path):
        for json_file in glob.glob(os.path.join(folder_path, './**/cs-teamscale.findings.ts.json'), recursive=True):
            file_path = json_file
            with open(file_path, 'r') as f:
                data_file = json.load(f)
                for each_data in data_file:
                    for each_findings_in_each_data in each_data["findings"]:
                        cs_teamscale_finding["PrjName"].append(folder_path.split("\\")[-1].split("/")[-1])
                        cs_teamscale_finding["CPSName"].append(
                            os.path.basename(os.path.dirname(os.path.dirname(file_path))))

                        cs_teamscale_finding["SWCName"].append(os.path.basename(os.path.dirname(file_path)))
                        cs_teamscale_finding["FilePath"].append(each_data['path'])
                        cs_teamscale_finding["Warning"].append(each_findings_in_each_data['message'])
                        cs_teamscale_finding["findingTypeId"].append(each_findings_in_each_data['findingTypeId'])
                        cs_teamscale_finding["uniqueId"].append(
                            each_findings_in_each_data['findingProperties']['uniqueId'])
        return cs_teamscale_finding


def arch_teamscale():
    arch_teamscale_finding = {
        "PrjName": [],
        "CPSName": [],
        "SWCName": [],
        "FilePath": [],
        "Warning": [],
        "findingTypeId": [],
        "uniqueId": [],
    }
    for file in os.listdir(folder_path):
        for json_file in glob.glob(os.path.join(folder_path, './**/arch-teamscale.findings.ts.json'), recursive=True):
            file_path = json_file
            with open(file_path, 'r') as f:
                data_file = json.load(f)
                for each_data in data_file:
                    for each_findings_in_each_data in each_data["findings"]:
                        arch_teamscale_finding["PrjName"].append(folder_path.split("\\")[-1].split("/")[-1])
                        arch_teamscale_finding["CPSName"].append(
                            os.path.basename(os.path.dirname(os.path.dirname(file_path))))

                        arch_teamscale_finding["SWCName"].append(os.path.basename(os.path.dirname(file_path)))
                        arch_teamscale_finding["FilePath"].append(each_data['path'])
                        arch_teamscale_finding["Warning"].append(each_findings_in_each_data['message'])
                        arch_teamscale_finding["findingTypeId"].append(each_findings_in_each_data['findingTypeId'])
                        arch_teamscale_finding["uniqueId"].append(
                            each_findings_in_each_data['findingProperties']['uniqueId'])
        return arch_teamscale_finding


def qac_teamscale():
    qac_teamscale_finding = {
        "PrjName": [],
        "CPSName": [],
        "SWCName": [],
        "FilePath": [],
        "Warning": [],
        "findingTypeId": [],
        "uniqueId": [],
    }
    for file in os.listdir(folder_path):
        for json_file in glob.glob(os.path.join(folder_path, './**/qac-teamscale.findings.ts.json'), recursive=True):
            file_path = json_file
            with open(file_path, 'r') as f:
                data_file = json.load(f)
                for each_data in data_file:
                    for each_findings_in_each_data in each_data["findings"]:
                        qac_teamscale_finding["PrjName"].append(folder_path.split("\\")[-1].split("/")[-1])
                        qac_teamscale_finding["CPSName"].append(
                            os.path.basename(os.path.dirname(os.path.dirname(file_path))))

                        qac_teamscale_finding["SWCName"].append(os.path.basename(os.path.dirname(file_path)))
                        qac_teamscale_finding["FilePath"].append(each_data['path'])
                        qac_teamscale_finding["Warning"].append(each_findings_in_each_data['message'])
                        qac_teamscale_finding["findingTypeId"].append(each_findings_in_each_data['findingTypeId'])
                        qac_teamscale_finding["uniqueId"].append(
                            each_findings_in_each_data['findingProperties']['uniqueId'])
        return qac_teamscale_finding


def modeladvisor():
    modeladvisor_finding = {
        "PrjName": [],
        "CPSName": [],
        "SWCName": [],
        "FilePath": [],
        "Warning": [],
        "findingTypeId": [],
    }
    for file in os.listdir(folder_path):
        for json_file in glob.glob(os.path.join(folder_path, './**/modeladvisor.findings.ts.json'), recursive=True):
            file_path = json_file
            with open(file_path, 'r') as f:
                data_file = json.load(f)
                for each_data in data_file:
                    for each_findings_in_each_data in each_data["findings"]:
                        modeladvisor_finding["PrjName"].append(folder_path.split("\\")[-1].split("/")[-1])
                        modeladvisor_finding["CPSName"].append(
                            os.path.basename(os.path.dirname(os.path.dirname(file_path))))

                        modeladvisor_finding["SWCName"].append(os.path.basename(os.path.dirname(file_path)))
                        modeladvisor_finding["FilePath"].append(each_data['path'])
                        modeladvisor_finding["Warning"].append(each_findings_in_each_data['message'])
                        modeladvisor_finding["findingTypeId"].append(each_findings_in_each_data['findingTypeId'])
        return modeladvisor_finding


if __name__ == '__main__':

    cs_teamscale_finding = None
    arch_teamscale_finding = None
    qac_teamscale_finding = None
    modeladvisor_finding = None

    cs_teamscale_finding = cs_teamscale()
    arch_teamscale_finding = arch_teamscale()
    qac_teamscale_finding = qac_teamscale()
    modeladvisor_finding = modeladvisor()

    with pd.ExcelWriter('report.xlsx', engine='openpyxl') as writer:
        if cs_teamscale_finding:
            pd.DataFrame.from_dict(cs_teamscale_finding).to_excel(writer, index=False, sheet_name="Codesonar")
        if arch_teamscale_finding:
            pd.DataFrame.from_dict(arch_teamscale_finding).to_excel(writer, index=False, sheet_name="Architecture")
        if qac_teamscale_finding:
            pd.DataFrame.from_dict(qac_teamscale_finding).to_excel(writer, index=False, sheet_name="QAC")
        if modeladvisor_finding:
            pd.DataFrame.from_dict(modeladvisor_finding).to_excel(writer, index=False, sheet_name="Model Advisor")

    formatted_excel = os.path.join(os.path.dirname(os.path.realpath(__file__)), "SW-findings-report.xlsx")
    writer = pd.ExcelWriter(formatted_excel, engine='xlsxwriter')
    dfs = {}
    print("\nFormatting the report")

    sheet_dict = pd.read_excel('report.xlsx', sheet_name=None)

    for sheet_name, df in sheet_dict.items():
        print(f"Sheet Name: {sheet_name}")
        print(df.head())
        print("\n" + "="*40 + "\n")

    if "codesonar" in finding_option.lower():
        dfs['Codesonar'] = pd.read_excel("report.xlsx", 'Codesonar')
    if "architecture" in finding_option.lower():
        dfs['Architecture'] = pd.read_excel("report.xlsx", "Architecture")
    if "qac" in finding_option.lower():
        dfs['QAC'] = pd.read_excel("report.xlsx", 'QAC')
    if "modeladvisor" in finding_option.lower():
        dfs['Model Advisor'] = pd.read_excel("report.xlsx", 'Model Advisor')

    for sheet in dfs.keys():
        dfs[sheet].to_excel(writer, sheet_name=sheet, index=False, na_rep=' ')
        for column in dfs[sheet]:
            column_length = max(dfs[sheet][column].astype(str).map(len).max(), len(column))
            col_idx = dfs[sheet].columns.get_loc(column)
            writer.sheets[sheet].set_column(col_idx, col_idx, column_length)

        workbook = writer.book
        worksheet = writer.sheets[sheet]
        worksheet.freeze_panes(1, 0)
        worksheet.autofilter('A1:G1')
        header_format_object = workbook.add_format({
            'bold': 'true',
            'valign': 'top',
            'fg_color': '#6495ED',
            'font_color': '#000000'})

        for col_number, value in enumerate(dfs[sheet].columns.values):
            worksheet.write(0, col_number, value,
                            header_format_object)

    workbook.close()
    print('Success')