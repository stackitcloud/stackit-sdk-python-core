> ⓘ INFO: The STACKIt Python SDK is in beta and in active development.


# STACKIT Python SDK Core

## Introduction

The STACKIT Python core package consists of core functionality which is needed
to use the [STACKIT Python SDK](https://github.com/stackitcloud/stackit-sdk-python).

## Compilation and Installation

You can install this package by running the following command from the root of the this repository:

```bash
make install
```

### Development Mode

When developing, you can use a feature of `pip` called _Editable Installs_,
which installs the local files like a package so you can test features without
reinstalling the package every time.
This package also defines additional depencies for development, like testing and linting.

Execute the following in the root folder of this repository:

```bash
make install-dev
```

## Usage

The core package does nothing on its own and must be used in conjunction with
the [STACKIT Python SDK](https://github.com/stackitcloud/stackit-sdk-python).