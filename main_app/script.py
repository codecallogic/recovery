import infermedica_api

infermedica_api.configure(app_id='dd7d8ffc', app_key='805d0529637017534b6b5726f942c5b9')

api = infermedica_api.get_api()

# conditions = api.conditions_list()

# print(api.condition_details('c_33'), end="\n\n")


request = infermedica_api.Diagnosis(sex='female', age=35)

request.add_symptom('s_88', 'present', initial=True)
request.add_symptom('s_105', 'present', initial=True)
request.add_symptom('s_98', 'present', initial=True)
request.add_symptom('s_100', 'present', initial=True)

# # call diagnosis
request = api.diagnosis(request)

print(request)

# print(conditions[0])
# print(api.symptom_details('s_13'), end="\n\n")
# print(api.search('fever'), end="\n\n")

# s_88 shortness of breath
# s_105 cough, dry
# s_98 fever
# s_102 cough

# api = infermedica_api.get_api()

# print(api.search('fever'), end="\n\n")
