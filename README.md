# 🖼️ StegoVault - Hide & Extract Text in Images with Password
Note: this document is written with the help of AI.

## 🔹 Overview
This project allows you to hide and extract text in images using steganography techniques. You can embed text from a PDF file or manual input into an image, and later extract it using a **secret key**.

## 🔹 Features

* ✅ Hide text inside an image without affecting its appearance with a password.
* ✅ Extract hidden text from an image using a password.
* ✅ Supports text input from PDF files or manual input.
* ✅ Optionally save extracted text as a PDF file.
* ✅ Simple CLI-based user interface for easy usage.

## 🔹 Installation

### 1. Install Dependencies

Ensure you have Python installed, then install the required libraries:

```bash
pip install numpy imageio PyMuPDF
```
### 2. Clone the Repository

```bash
git clone 
cd 
```

## 🔹 Usage

Run the CLI script:

```bash
python steganography_cli.py
```

### 1. Hide Text in an Image

* Choose Option 1 in the menu.
* Provide the image file path.
* Enter a secret key for encoding.
* Select PDF file or manual input.
* Provide the output image filename where the encoded image will be saved.

### 2. Extract Text from an Image

* Choose Option 2 in the menu.
* Provide the encoded image file path.
* Enter the secret key to extract text.
* Choose whether to save the extracted text as a PDF file.

### 3. Exit the Program

* Choose Option 3 to exit.

## 🔹 Example Usage

🔹 Welcome to StegoVault - Hide & Extract Text in Images! 🔹

```bash
What would you like to do?
1️⃣ Hide text in an image
2️⃣ Extract text from an image
3️⃣ Exit

Enter your choice (1/2/3): 1

📷 Enter the image path to hide text: input_image.png
🔑 Enter a secret key to secure the text: mysecretkey

Would you like to embed text from:
1️⃣ A PDF file
2️⃣ Manual input
Enter choice (1/2): 2

✏️ Enter the text to hide: Hello, world!
💾 Enter output image file name (e.g., hidden_image.png): hidden_image.png

✅ Text successfully hidden in hidden_image.png!
```

## 🔹 Requirements

* Python 3.x
* numpy
* imageio
* PyMuPDF (for PDF handling)

## 🔹 Future Work & Upcoming Features 
* Steganography for Videos → Instead of just images, users will be able to embed text into videos.
* Password Authentication via Video → The password will be hashed using SHA-256 and steganographically hidden in the first frame of a video. The system will authenticate the password before allowing text extraction.
* Advanced Encoding Using Password-Based Mapping → Instead of hiding text sequentially, the text embedding will follow a custom pattern based on the password, making it even more secure.

## 🔹 Troubleshooting
❌ "ModuleNotFoundError: No module named 'imageio'"

✅ Run:

```bash
pip install imageio
```

❌ "Image is too small to hide text"
✅ Use a larger image with more pixels.

## 🔹 Notice 
This project, including the code and documentation, was developed with the assistance of AI, using proper prompts, code reviews, and manual editing to ensure accuracy and functionality. While AI provided guidance, all implementations and refinements were reviewed and optimized for best performance.

## 🔹 Contributing

Feel free to contribute by submitting issues or pull requests! 🚀

🔹 License

MIT License © 2025

💡 Author: Ziad Assem

📧 Contact: zeyad.asem.m@gmail.com

🔗 GitHub: [ziadasem](https://github.com/ziadasem)

💼 Linkedin: [Ziad Assem](https://www.linkedin.com/in/ziad-assem/)