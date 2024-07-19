# J.A.R.V.I.S
 J.A.R.V.I.S Project

 Overview
This project utilizes various Python libraries and frameworks to create a generative AI application. It includes Kivy for building the GUI, Hugging Face's Transformers for natural language processing, and Flask for web integration.

 Technologies Used
- Python: Programming language used for development.
- Kivy: A library for developing multitouch applications. It provides a rich user interface.
- Transformers: A library by Hugging Face that provides pre-trained models for various NLP tasks.

 Setting Up the Environment
1. Create a Virtual Environment:
   ```bash
   python -m venv myenv
   ```
2. Activate the Environment:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

3. Install Required Packages:
   ```bash
   pip install kivy  transformers tf-keras
   ```

 Running the Application
- To run the main application, use:
  ```bash
  python main2.py
  ```

 Troubleshooting
- If you encounter issues with package versions, make sure to check for compatibility, especially with Keras and TensorFlow.
- For any library that isn't installed, you can add it using pip, e.g.:
  ```bash
  pip install package-name
  ```

 Additional Notes
- Consider enabling Windows Developer Mode for better compatibility with symlinks used in caching (for Hugging Face).
- If any models require TensorFlow or PyTorch, make sure to install the required version:
  ```bash
  pip install tensorflow
   or
  pip install torch
  ```

 Acknowledgements
- Special thanks to the A2SV community for their support in Data Structures and Algorithms.
- Appreciation for resources from Hugging Face and Kivy documentation.
