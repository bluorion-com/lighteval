# MIT License

# Copyright (c) 2024 The HuggingFace Team

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import setuptools
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

setuptools.setup(
    name="lighteval",
    version="0.3.0",
    packages=setuptools.find_packages(),
    cmdclass=(
        {
            "bdist_wheel": _bdist_wheel,
        }
    ),
    include_package_data=True,
    package_data={"lighteval/metrics": ["lighteval/metrics/*.jsonl"]},
    install_requires=[
        # Base dependencies
        "transformers>=4.38.0",
        "huggingface_hub>=0.23.0",
        "torch>=2.0",
        "GitPython>=3.1.41",  # for logging
        "datasets>=2.14.0",
        # Prettiness
        "termcolor==2.3.0",
        "pytablewriter",
        "colorama",
        # Extension of metrics
        "aenum==3.1.15",
        # Base metrics
        "nltk==3.8.1",
        "scikit-learn",
        "spacy==3.7.2",
        "sacrebleu",
        "rouge_score==0.1.2",
        "sentencepiece>=0.1.99",
        "protobuf==3.20.*",  # pinned for sentencepiece compat
        "pycountry",
    ],
)
