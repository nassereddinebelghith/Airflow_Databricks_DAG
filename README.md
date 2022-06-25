<!-- PROJECT SHIELDS -->
[![GPL License][license-shield]][license-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![Code Size][cSize-shield]][cSize-url]


<!-- PROJECT LOGO -->
<br />
  <h3 align="center">ezBMI</h3>

  <p align="center">
    A super simple & sleek BMI calculator to keep track of your health!
    <br />
    <a href="https://github.com/jlemanski1/BMI-Calculator/"><strong>Checkout the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jlemanski1/BMI-Calculator/releases">Download</a>
    ·
    <a href="https://github.com/jlemanski1/BMI-Calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/jlemanski1/BMI-Calculator/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


<!-- ABOUT THE PROJECT -->
## About The Project

[![ezBMI][app-screenshot1]](#)

There are many great BMI calculators available on the appstore, however, I couldn't find one that really suited my needs so I created this super simple one based off a neat design I found on dribbble. I want to create a BMI calculator so quick and easy to use that you never get lazy about checking.

Here's why:
* Your fitness apps shouldn't get in the way of your active lifestyle
* You shouldn't be doing simple tasks using bloated slow apps

Of course, I also wanted to try to implement a concept design through the use of custom Widgets. Mainly as a good learning exercise, but also to be able to build a collection of custom Widgets that I can reuse and further customize for future apps. Aaaaaand, of course, the sleek design I found on dribbble is Simple Bmi Calculator by [Ruben Vaalt](https://dribbble.com/shots/4585382-Simple-BMI-Calculator)

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With
* [Dart](https://dart.dev/)
* [Flutter](https://flutter.dev/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Install Flutter](https://flutter.dev/docs/get-started/install/linux)
* Dart
```sh
sudo apt update && sudo apt install dart
```

### Installation

Available now on the [Play Store](https://play.google.com/store/apps/details?id=tech.jlemanski.bmi_calculator), alternatively:

1. Clone the repo
```sh
git clone https://github.com/jlemanski1/BMI-Calculator.git
```
2. Run flutter doctor to ensure everything is setup correctly
```sh
cd bmi_calculator
flutter doctor
```
3. Build APK
```sh
flutter build apk --split-per-abi --release
```
4. Install APK to device
```sh
flutter install
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/jlemanski1/BMI-Calculator/issues) for a list of proposed features (and known issues).
You can also check out the [project board](https://github.com/jlemanski1/BMI-Calculator/projects/1)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jonathan Lemanski - lemanskij@mymacewan.ca

Project Link: [https://github.com/jlemanski1/BMI-Calculator/](https://github.com/jlemanski1/BMI-Calculator/)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Ruben Vaalt](https://dribbble.com/shots/4585382-Simple-BMI-Calculator) for the design
* App icon made by [Nikita Golubev](https://www.flaticon.com/authors/nikita-golubev) from [www.flaticon.com](www.flaticon.com)
* [Flutter Docs](https://flutter.dev/docs) for help with all things Flutter


<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/jlemanski1/BMI-Calculator
[license-url]: https://github.com/jlemanski1/BMI-Calculator/blob/master/LICENSE
[issues-shield]: https://img.shields.io/github/issues/jlemanski1/BMI-Calculator
[issues-url]: https://github.com/jlemanski1/BMI-Calculator/issues
[forks-shield]: https://img.shields.io/github/forks/jlemanski1/BMI-Calculator
[forks-url]: https://github.com/jlemanski1/BMI-Calculator/network/members
[cSize-shield]: https://img.shields.io/github/languages/code-size/jlemanski1/BMI-Calculator
[cSize-url]: https://github.com/jlemanski1/BMI-Calculator
[app-screenshot1]: images/bmi_01.png
[app-screenshot2]: images/bmi_02.png
[app-screenshot3]: images/bmi_03.png
