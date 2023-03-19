import openai
import PyPDF2

# 在 OpenAI 网站上创建一个 API Key，并将其复制到此处
openai.api_key = "<key>"
openai.api_base = "<endpint>"
openai.api_type = "azure"
openai.api_version = "2022-12-01"

# 打开PDF文件
pdfFileObj = open('migrate_to_azure_jboss_eap_vm.pdf', 'rb')

# 创建一个PDF文件阅读器（reader）对象
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# 获取PDF文件的页数
numPages = len(pdfReader.pages)

# 定义一个空字符串，用于存储PDF文件的所有文本内容
pdfText = ""

# 循环遍历PDF文件中的每一页，并将文本内容添加到pdfText变量中
for i in range(numPages):
    # 获取当前页的内容
    pageObj = pdfReader.pages[i]

    # 提取当前页的文本内容
    pageText = pageObj.extract_text()

    # 将文本内容添加到pdfText变量中
    pdfText += pageText

# 关闭PDF文件
pdfFileObj.close()

prompt = "<|im_start|>system\nThe system is an AI assistant that helps people find information.\n<|im_end|>\n<|im_start|>user\n"
prompt += "based on the following content, generate a migration guide with details of migrating WebLogic application to Azure: \n"
prompt += pdfText
prompt += "\n<|im_end|>\n<|im_start|>assistant"

# 将PDF文件的文本内容传递给OpenAI GPT模型，并生成大纲
response = openai.Completion.create(
    engine="chat",
    prompt=prompt,
    max_tokens=2048,
    temperature=1,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["<|im_end|>"]
)

# 打印生成的大纲
print(response.choices[0].text)