import testrail as tr
import logging
import PySimpleGUI as Sg

dd_get_api = ['get_plan', 'get_plans', 'get_run',
              'get_runs',  'get_test', 'get_cases',
              'get_suite', 'get_suites', 'get_project',
              'get_projects', 'get_statuses', 'get_tests']

layout = [[Sg.DropDown(dd_get_api)]]
main_layout = [[Sg.DropDown(dd_get_api, key='dd_get'),
                  Sg.Text('Case #'), Sg.InputText(key='case_number'),
                  Sg.Button("Request Data", key='get_data')]]


class TestRail(object):
    def __init__(self, tr_endpoint, tr_user, tr_pw):
        self.client = tr.APIClient(tr_endpoint)
        self.client.user = tr_user
        self.client.password = tr_pw

    def __get__(self, instance, owner):
        return self.client, self.client.user, self.client.password

    # for quick resets:
    def __set__(self, instance, tr_endpoint, tr_user, tr_pw):
        self.client = tr.APIClient(tr_endpoint)
        self.client.user = tr_user
        self.client.password = tr_pw

    def __str__(self):
        return "Client {} connected through {}".format(self.client,
                                                       self.client.user)

    def tr_status(self, tr_status_summary, tr_result):
        result = self.client.send_post(
                '{}/1/1',
                {'status_id': 1, 'comment': '{}'.format(
                        tr_status_summary, tr_result)})

    def tr_screenshot(self, tr_ss_summary, tr_ss):
        try:
            result = self.client.send_post('{}/1}',
                                           '{}}'.format(tr_ss_summary, tr_ss))
            logging.info("Pushed TR SS: {}, {} , Result: {}".format(
                    tr_ss_summary, tr_ss, result))
        except:
            logging.error("Error Pushing TR SS: {}".format(result))


ok = TestRail("URL", "UN",
              "PW")

main_window = Sg.Window(title='TR API TEST', layout=main_layout)

while True:
    b, v = main_window.Read(timeout=0)

    if b == 'get_data':
        try:
            get_data = ok.client.send_get('{}/{}'.format(v['dd_get'],
                                                     v['case_number']))
            print(get_data)
        except (tr.APIError) as error:
            Sg.PopupOK('TestRail API Error', error)

    if b == 'exit' or None:
        quit()
