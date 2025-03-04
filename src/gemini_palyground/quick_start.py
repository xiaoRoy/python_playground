from google import genai
from google.genai import types
import json_loader
from setup_gemini import setup_gemini, ROLE_USER

client = setup_gemini()


# response = client.models.generate_content(model="gemini-2.0-flash", contents="tell me about RAG")

# print(response.text)


def get_completion(prompt, model="gemini-2.0-flash", temperature=0.0):
    generate_content_config = types.GenerateContentConfig(temperature=temperature, system_instruction=[
        types.Part.from_text(
            text="")
    ])
    contents = [types.Content(role=ROLE_USER, parts=[types.Part.from_text(text=prompt)])]

    responses = client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config
    )
    return responses


def show_completion_result(prompt, model="gemini-2.0-flash", temperature=0.0):
    responses = get_completion(prompt, model, temperature)
    for chunk in responses:
        print(chunk.text, end="")


class Prompt:
    KEY_PROMPT_TEXT = "text"
    KEY_PROMPT_TEMPLATE = "prompt_template"
    PROMPTS_FILE_PATH = "./prompts.json"

    def __init__(self, text, template):
        self.text = text
        self.template = template

    def compose_prompt(self):
        return self.template.format(self.text)

    @staticmethod
    def generate_prompt(prompt_spec_name):
        prompt_spec = json_loader.load_prompt_from_json(Prompt.PROMPTS_FILE_PATH, prompt_spec_name)
        return Prompt(prompt_spec.get(Prompt.KEY_PROMPT_TEXT), prompt_spec.get(Prompt.KEY_PROMPT_TEMPLATE))

    @staticmethod
    def generate_prompt_for_product_review(template_name, review_index=0):
        product_review = json_loader.load_prompt_from_json(Prompt.PROMPTS_FILE_PATH, "product_review")
        return Prompt(product_review.get("reviews")[review_index], product_review.get("template").get(template_name))

    @staticmethod
    def generate_prompt_for_lamp_review(template_name):
        return Prompt.generate_prompt_for_multiple_prompt_templates("lamp_review", template_name)

    @staticmethod
    def generate_prompt_for_multiple_prompt_templates(spec_name, template_name):
        lamp_review = json_loader.load_prompt_from_json(Prompt.PROMPTS_FILE_PATH, spec_name)
        text = lamp_review.get("text")
        template = lamp_review.get("template").get(template_name)
        return Prompt(text, template)


def load_prompt_spec(prompt_spec_name):
    prompt_template_file_path = "./prompts.json"
    return json_loader.load_prompt_from_json(prompt_template_file_path, prompt_spec_name)


def ues_delimiters_in_prompt():
    prompt = Prompt.generate_prompt("delimiters")
    show_completion_result(prompt=prompt.compose_prompt())


def ask_for_structure_output():
    prompt = Prompt.generate_prompt("structure_output")
    show_completion_result(prompt=prompt.compose_prompt())


def check_conditions():
    prompt = Prompt.generate_prompt("check_conditions")
    show_completion_result(prompt=prompt.compose_prompt())


def few_shot():
    prompt = Prompt.generate_prompt("few_show")
    show_completion_result(prompt=prompt.compose_prompt())


def step_by_step():
    prompt = Prompt.generate_prompt("step_by_step")
    show_completion_result(prompt=prompt.compose_prompt())


def model_thinks():
    prompt = Prompt.generate_prompt("model_think")
    show_completion_result(prompt=prompt.compose_prompt())


def summarize():
    prompt = Prompt.generate_prompt_for_product_review("summarize")
    show_completion_result(prompt=prompt.compose_prompt())


def extract():
    prompt = Prompt.generate_prompt_for_product_review("extract")
    show_completion_result(prompt=prompt.compose_prompt())


def summarize_more():
    for index in range(4):
        prompt = Prompt.generate_prompt_for_product_review("more", review_index=index)
        show_completion_result(prompt=prompt.compose_prompt())


def inferring():
    prompt = Prompt.generate_prompt_for_lamp_review("inferring")
    show_completion_result(prompt=prompt.compose_prompt())


def inferring_case_2():
    prompt = Prompt.generate_prompt_for_lamp_review("inferring_case_2")
    show_completion_result(prompt=prompt.compose_prompt())


def inferring_case_3():
    prompt = Prompt.generate_prompt_for_lamp_review("inferring_case_3")
    show_completion_result(prompt=prompt.compose_prompt())


def inferring_case_4():
    prompt = Prompt.generate_prompt_for_lamp_review("inferring_case_4")
    show_completion_result(prompt=prompt.compose_prompt())


def inferring_case_5():
    prompt = Prompt.generate_prompt_for_lamp_review("inferring_case_5")
    show_completion_result(prompt=prompt.compose_prompt())


def infer_topics():
    prompt = Prompt.generate_prompt_for_multiple_prompt_templates("topic", "infer_topic")
    result = get_completion(prompt=prompt.compose_prompt())
    topics = []
    for chunk in result:
        topics.extend(chunk.text.split(sep=","))
    print(topics)


def infer_more():
    prompt = Prompt.generate_prompt_for_multiple_prompt_templates("topic", "infer_more")
    show_completion_result(prompt.compose_prompt())


def translate():
    prompt = Prompt.generate_prompt("translate")
    show_completion_result(prompt=prompt.compose_prompt())


def identify_language():
    prompt = Prompt.generate_prompt("identify_language")
    show_completion_result(prompt=prompt.compose_prompt())


def translate_multiple():
    prompt = Prompt.generate_prompt("translate_multiple")
    show_completion_result(prompt=prompt.compose_prompt())


def translate_in_forms():
    prompt = Prompt.generate_prompt("translate_in_forms")
    show_completion_result(prompt=prompt.compose_prompt())


def universal_translator():
    prompt = Prompt.generate_prompt("universal_translator")
    show_completion_result(prompt=prompt.compose_prompt())


def tone_transformation():
    prompt = Prompt.generate_prompt("tone_transformation")
    show_completion_result(prompt=prompt.compose_prompt())


def format_transformation():
    prompt = Prompt.generate_prompt("format_transformation")
    show_completion_result(prompt=prompt.compose_prompt())


def grammar_check():
    prompt = Prompt.generate_prompt("grammar_check")
    show_completion_result(prompt=prompt.compose_prompt())


def rewrite_review():
    prompt = Prompt.generate_prompt("rewrite_review")
    show_completion_result(prompt=prompt.compose_prompt())


def auto_replay_review():
    prompt = Prompt.generate_prompt("auto_replay_review")
    show_completion_result(prompt=prompt.compose_prompt(), temperature=0.7)


auto_replay_review()
