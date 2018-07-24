import json

def json_to_data(json_str):
    """
    对Json数据进行处理
    """
    data = json.loads(json_str)
    for cases in data:
        print(cases)
        case_list = []
        cases_dict = {}
        for case in data[cases]:
            case_tup = tuple(case.values())
            case_list.append(case_tup)
        cases_dict[cases]= case_list
    return cases_dict


if __name__ == '__main__':
    data = {
        "test_search": [
            {
                "case_id": "tc001_baidu_search.01",
                "search_key": "unittest",
                "assert_title": "unittest_百度搜索"
            },
            {
                "case_id": "tc001_baidu_search.02",
                "search_key": "selenium",
                "assert_title": "selenium_百度搜索"
            },
            {
                "case_id": "tc001_baidu_search.03",
                "search_key": "data driver",
                "assert_title": "data driver_百度搜索"
            }
        ]
    }
    d = json_to_data(data)
    print(d["test_search"])