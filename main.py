import os
from text_in_image_steganographer import TextInImageSteganographer

def main():
    stego = TextInImageSteganographer()
    
    print("\n🔹 Welcome to StegoVault - Hide & Extract Text in Images! 🔹\n")
    
    while True:
        print("\nWhat would you like to do?")
        print("1️⃣ Hide text in an image")
        print("2️⃣ Extract text from an image")
        print("3️⃣ Exit")
        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            image_path = input("\n📷 Enter the image path to hide text: ").strip()
            key_text = input("🔑 Enter a secret key to secure the text: ").strip()

            source_choice = input("\nWould you like to embed text from:\n1️⃣ A PDF file\n2️⃣ Manual input\nEnter choice (1/2): ").strip()

            if source_choice == "1":
                pdf_path = input("\n📄 Enter the PDF file path: ").strip()
                text = None
            elif source_choice == "2":
                text = input("\n✏️ Enter the text to hide: ").strip()
                pdf_path = None
            else:
                print("\n❌ Invalid choice. Try again.")
                continue

            output_image = input("\n💾 Enter output image file name (e.g., hidden_image.png): ").strip()

            try:
                stego.hide_text_in_image(key_text, image_path, pdf_path, text, output_image)
                print(f"\n✅ Text successfully hidden in {output_image}!\n")
            except Exception as e:
                print(f"\n❌ Error: {e}")

        elif choice == "2":
            image_path = input("\n📷 Enter the image path to extract text: ").strip()
            key_text = input("🔑 Enter the secret key: ").strip()
            save_pdf = input("\n💾 Do you want to save extracted text as a PDF? (yes/no): ").strip().lower()

            pdf_output = None
            if save_pdf == "yes":
                pdf_output = input("📄 Enter the output PDF file name: ").strip()

            try:
                extracted_text = stego.extract_text_from_image(key_text, image_path, pdf_output)
                print("\n📝 Extracted Text:\n" + extracted_text)
                
                if pdf_output:
                    print(f"\n✅ Text saved as {pdf_output}!")
            except Exception as e:
                print(f"\n❌ Error: {e}")

        elif choice == "3":
            print("\n👋 Exiting... Have a great day!")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
