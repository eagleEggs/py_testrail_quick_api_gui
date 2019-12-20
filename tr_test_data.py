import PySimpleGUI as Sg


# GET API:
dd_get_api = ['get_plan', 'get_plans', 'get_run',
              'get_runs',  'get_test', 'get_case', 'get_cases',
              'get_suite', 'get_suites', 'get_project',
              'get_projects', 'get_statuses', 'get_tests',
              'get_results', 'get_results_for_case', 'get_results_for_run',
              'get_attachments_for_case', 'get_attachments_for_test',
              'get_attachment']

# ADD / MOD / DEL API:
dd_cases_api = [
            'add_case',
            'update_case',
            'delete_case']

dd_runs_api = [
            'add_run',
            'update_run',
            'close_run',
            'delete_run']

dd_results_api = [
            'add_result',
            'add_result_for_case',
            'add_results',
            'add_results_for_cases']

dd_attachments_api = [
                'add_attachment_to_result',
                'delete_attachment']

layout = [[Sg.DropDown(dd_get_api)]]
main_layout = [[Sg.DropDown(dd_get_api, key='dd_get'),
                  Sg.Text('Case #'), Sg.InputText(key='case_number'),
                  Sg.Button("Request Data", key='get_data')]]

