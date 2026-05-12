
import subprocess
import pkg_resources


#gerekli kutuphaneleri kontrol etme

def install_if_needed(package, version):
    try:
        pkg = pkg_resources.get_distribution(package)
        if pkg.version != version:
            raise pkg_resources.VersionConflict(pkg, version)
    except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
        subprocess.check_call(["pip", "install", f"{package}=={version}"])

install_if_needed("langchain-core", "0.3.72")
install_if_needed("langchain-openai", "0.3.28")
install_if_needed("langchain-community", "0.3.27")
install_if_needed("unstructured", "0.18.11")
install_if_needed("langchain-chroma", "0.2.5")
install_if_needed("langchain-text-splitters", "0.3.9")
install_if_needed("pydantic", "2.11.9")

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import os

loader = UnstructuredHTMLLoader(file_path="data/mg-zs-warning-messages.html")
car_docs = loader.load()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=os.environ["////////////api////////////"])

# Metni bolme
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(car_docs)

# Metni Chromaya kaydetme
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Retriever kurma, gidip gerekli parcayi bulacak
retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_template(
    "Sen soru-cevap görevleri için bir asistansın. Soruyu cevaplamak için aşağıdaki döküman parçalarını kullan. "
    "Eğer cevabı bilmiyorsan, bilmediğini söyle. En fazla üç cümleyle kısa ve öz, Türkçe olarak cevap ver.\n"
    "Soru: {question} \n"
    "Kaynak Metin: {context} \n"
    "Cevap:"
)


# soru > Doc Bul > Prompt ekle > run model > Cevap ver
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# soru
query = "The Gasoline Particular Filter Full warning has appeared. What does this mean and what should I do about it?"

answer = rag_chain.invoke(query).content

print(answer)