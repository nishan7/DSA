import os
import re
from collections import defaultdict

import marko
import reusables
from pathvalidate import sanitize_filename
from slugify import slugify

file_text = open('data.txt').read()

# all_questions = reusables.load_json('data.json')
all_questions = defaultdict(dict)


def create_filesystem(topic_name, all_questions):
    if not os.path.exists('./Data/{}'.format(topic_name)):
        os.mkdir('./Data/{}'.format(topic_name))

    if topic_name == 'Java':
        EXT = 'java'
    else:
        EXT = 'py'

    for question_name, question_value in all_questions[topic_name].items():
        question_value['question_name'] = question_value['question_name'].strip('!')
        link = question_value['link']
        sub_questions = question_value['sub_questions']

        if EXT == 'py':
            markdown_info = """'''\n#### Name:  {}\nLink: [link]({})\n\n'''""".format(question_name, link)
        elif EXT == 'java':
            markdown_info = """/*\n#### Name:  {}\nLink: [link]({})\n\n*/""".format(question_name, link)

        # info_md = """\n#### Name:  {}\nLink: [link]({})\n\n""".format(question_name, link)

        if not os.path.exists('Data/{}/{}'.format(sanitize_filename(topic_name), sanitize_filename(question_name), )):
            os.mkdir('Data/{}/{}'.format(sanitize_filename(topic_name), sanitize_filename(question_name), ))

        py_file = 'Data/{}/{}/{}.{}'.format(sanitize_filename(topic_name), sanitize_filename(question_name),
                                            sanitize_filename(question_name), EXT)
        # md_file = sanitize_filename(        'Data/{}/{}/{}.md'.format(topic_name, question_name, question_name))

        if not os.path.exists(py_file) and not question_value['is_blank']:
            print(question_name)
            with open(py_file, 'w') as fp:
                fp.write(markdown_info)

        all_questions[topic_name][question_name]['path'] = os.path.abspath(py_file)

        # if not os.path.exists(md_file):
        #     with open(md_file, 'w') as fp:
        #         fp.write(info_md)

        for idx, sub_question in enumerate(sub_questions):
            sub_question_name = sub_question['sub_question_name']
            sub_question_link = sub_question['link']

            if EXT == 'py':
                markdown_info = """'''\n#### Name:  {}\nLink: [link]({})\n\n#### Sub_question_name: {} \nLink: [link]({})\n\n'''""".format(
                    question_name, link, sub_question_name, sub_question_link)
            elif EXT == 'java':
                markdown_info = """/*\n#### Name:  {}\nLink: [link]({})\n\n#### Sub_question_name: {} \nLink: [link]({})\n\n*/""".format(
                    question_name, link, sub_question_name, sub_question_link)

            # info_md = """\n#### Name:  {}\nLink: [link]({})\n\n#### Sub_question_name: {} \nLink: [link]({})\n\n """.format(
            #     question_name, link,
            #     sub_question_name,
            #     sub_question_link)

            if not os.path.exists(
                    'Data/{}/{}'.format(sanitize_filename(topic_name), sanitize_filename(question_name), )):
                os.mkdir('Data/{}/{}'.format(sanitize_filename(topic_name), sanitize_filename(question_name), ))

            py_file = 'Data/{}/{}/{}.{}'.format(sanitize_filename(topic_name), sanitize_filename(question_name),
                                                sanitize_filename(sub_question_name), EXT)

            # md_file = sanitize_filename('Data/{}/{}/{}.md'.format(topic_name, question_name, sub_question_name))

            if not os.path.exists(py_file):
                with open(py_file, 'w') as fp:
                    fp.write(markdown_info)
            all_questions[topic_name][question_name]['sub_questions'][idx]['path'] = os.path.abspath(py_file)

            # if not os.path.exists(md_file):
            #     with open(md_file, 'w') as fp:
            #         fp.write(info_md)
    return all_questions


# Questions to stack
def parse_txt_file(stack, all_questions):
    questions = {}
    topics = []
    sub_questions = []
    while stack:
        item = stack.pop()
        if item[0] == 'sub_question':
            sub_questions.append(item[1])
        elif item[0] == 'question':
            question = item[1]
            question.update({'sub_questions': sub_questions})
            question['is_blank'] = question['question_name'].endswith('!')
            question['question_name'] = question['question_name'].strip('!')
            questions[question['question_name']] = question
            sub_questions = []
        elif item[0] == 'topic':
            topic_name = item[1]
            topics.append(topic_name)
            all_questions[topic_name].update(questions)
            all_questions = create_filesystem(topic_name, all_questions)
            questions = {}

    old_topics = set(all_questions.keys()) - set(topics)
    for topic in old_topics:
        del all_questions[topic]
    return {topic_name: all_questions[topic_name] for topic_name in topics}  # Put the dictionary in order of topics


# It scrapes data.txt for questions
def get_data():
    stack = []
    for line in file_text.split('\n'):
        line = line.strip()
        # print(line)
        if line:
            if line.startswith('#'):
                stack.append(('topic', line[1:].lstrip()))
            elif line.startswith('.'):
                match = re.match(r'(.*)\s(http?.*)$', line[1:].lstrip())
                if match:
                    sub_question = {'sub_question_name': match.group(1), 'link': match.group(2), 'path': ''}
                else:
                    sub_question = {'sub_question_name': line[1:].lstrip(), 'link': '', 'path': ''}

                stack.append(('sub_question', sub_question))
            else:
                match = re.match(r'(.*)\s(http?.*)$', line.lstrip())
                if match:
                    sub_question = {'question_name': match.group(1), 'link': match.group(2), 'path': ''}
                else:
                    sub_question = {'question_name': line.lstrip(), 'link': '', 'path': ''}
                stack.append(('question', sub_question))

    # pprint(stack)
    json = parse_txt_file(stack, all_questions)
    reusables.save_json(json, 'data.json', indent=2, )
    # pprint(json)
    return json


# It uses regex to get Description from py file
def get_code_and_info_from_py(file_path):
    if file_path.endswith('py'):
        pattern = r"[\'\"]{3}(.*?)['\"]{3}(.*)"
    else:
        print(file_path)
        pattern = r"/\*\s*.*?(.*)\*/\s*(.*)"
    # print(file_path)
    f = open(file_path).read()
    matches = re.search(pattern, f, re.MULTILINE | re.DOTALL)

    if matches:
        if len(matches.groups()) >= 2:
            return matches.group(2).strip(), marko.convert(matches.group(1))
        return '', marko.convert(matches.group(0))

    return f, ''


def get_data_for_html():
    json = get_data()
    # pprint(json)
    topics = list(json.keys())
    final_data = {}
    for topic, questions in json.items():
        final_questions = {}
        for question_name, question in questions.items():
            final_question = {}

            final_question['question_name'] = question['question_name']
            final_question['link'] = question['link']
            final_question['path'] = question['path']
            final_question['info'] = ''

            final_sub_questions = []
            if not question['is_blank']:
                code, info = get_code_and_info_from_py(final_question['path'])
                final_sub_questions.append({'id': slugify(final_question['path']),
                                            'sub_question_name': final_question['question_name'],
                                            'info': info,
                                            'code': code,
                                            'link': final_question['link'],
                                            'path': final_question['path']
                                            })

            for sub_question in reversed(question['sub_questions']):
                code, info = get_code_and_info_from_py(sub_question['path'])
                final_sub_questions.append({'id': slugify(sub_question['path']),
                                            'sub_question_name': sub_question['sub_question_name'],
                                            'link': sub_question['link'],
                                            'path': sub_question['path'],
                                            'info': info,
                                            'code': code,

                                            })
                # print(sub_question['path'])

            final_question['sub_questions'] = final_sub_questions
            # pprint(final_sub_questions)
            final_questions[question_name] = final_question

        final_data[topic] = final_questions
    return final_data, topics


if __name__ == '__main__':
    # get_data_for_html()
    print(get_data())
