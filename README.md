# Image Editor App - UI & Feature Mockup

This document outlines the mockdown/blueprint for the **Image Editor 😊** desktop application built with PyQt5 and Pillow.

---

## 1. Window Specifications
* **Dimensions:** 800px width × 550px height
* **Theme & Styling:** 
  * **Global Background:** Green shade (`#34813F`)
  * **Text Color:** Light mint (`#EFFFF1`)
  * **Font Family:** Times New Roman (20px base size)

---

## 2. Layout Wireframe

The application uses a master-detail split layout (`QHBoxLayout`) divided into two primary columns:

```text
+--------------------------------------------------------------------------+
| Image Editor 😊                                                      [X] |
+------------------------------------+-------------------------------------+
|                                    |                                     |
|  [     Folder     ] (Blue)         |                                     |
|  +------------------------------+  |                                     |
|  |                              |  |                                     |
|  |                              |  |               Image                 |
|  |      lw_files                |  |           (QLabel Area)             |
|  |    (ListWidget of            |  |      Background: #55A45F            |
|  |     supported images)        |  |                                     |
|  |                              |  |                                     |
|  |                              |  |                                     |
|  +------------------------------+  |                                     |
|                                    |                                     |
|                                    +-------------------------------------+
|                                    | [Left] [Right] [Mirror] [Sharp] [BW]|
|                                    |              (Tool Bar)             |
+------------------------------------+-------------------------------------+
   (Col 1: Width 20%)                  (Col 2: Width 80%)
```

---

## 3. Component Breakdown & Functionality

### Column 1 (Navigation & Selection - 20% Width)
1. **Folder Button (`btn_dir`)**:
   * **Style ID:** `btnFolder` (Distinct blue background `#32369A`)
   * **Action:** Opens a system directory dialog (`QFileDialog`) and loads filtered files (`.jpg`, `.png`, `.jpeg`, `.gif`) into the list widget.
2. **File List (`lw_files`)**:
   * Displays all valid image filenames from the selected working directory.
   * **Interaction:** Selecting an item triggers `currentRowChanged`, instantly loading and rendering the selected image onto the preview canvas.

### Column 2 (Canvas & Toolbar - 80% Width)
1. **Image Preview Area (`lb_image`)**:
   * **Default Text:** `'Image'`
   * **Background Color:** `#55A45F`
   * **Behavior:** Automatically scales loaded images using `Qt.KeepAspectRatio` to fit the current label bounds.
2. **Action Toolbar (`row_tools`)**:
   * **Left (`btn_left`):** Rotates the active image counter-clockwise by $90^\circ$ (using `ROTATE_90`), saves to the `Modified/` folder, and re-renders.
   * **Right (`btn_right`):** Rotates the active image clockwise by $90^\circ$ (using `ROTATE_270`), saves, and re-renders.
   * **Mirror (`btn_mirror`):** Flips the image horizontally (`FLIP_LEFT_RIGHT`), saves, and re-renders.
   * **Sharpness (`btn_sharp`):** Applies a sharpness filter (`SHARPEN`), saves, and re-renders.
   * **B/W (`btn_bw`):** Converts the image to grayscale (`"L"` mode), saves, and re-renders.

---

## 4. UI Style Sheet Reference

```css
QWidget {
    background-color: #34813F;
    color: #EFFFF1;
    font-family: "Times New Roman";
    font-size: 20px;
}
QLabel {
    background-color: #55A45F;
}
QPushButton {
    background-color: #339966;
    border-radius: 4px;
}
QPushButton::hover {
    background-color: #3CB679;
}
QPushButton#btnFolder {
    background-color: #32369A;
}
```