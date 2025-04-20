def calcNewHeightImg(size=(0, 0), width=0):
    return (size[1] / size[0]) * width


def calcAspectRatioImg(size=(0, 0)):
    return size[0] / size[1]


def resizeToSquareImg(aspectRatio, containerSize):
    newWidth = 0
    newHeight = 0
    if aspectRatio > 1:
        newWidth = containerSize
        newHeight = containerSize / aspectRatio
        return (newWidth, newHeight)
    else:
        newWidth = containerSize * aspectRatio
        newHeight = containerSize
        return (newWidth, newHeight)


def updateSliderPosition(function, value, slider):
    if not value:
        return
    value =  float(value)
    function(value)
    slider.set(value)


def updateEntryValue(function, value, entry):
    function(value)
    entry.delete(0, 7)
    entry.insert(index=0, string=str(value))


# def updateHandler(fuction, value, handler):
#     fuction(value)
#     if handler.winfo_class() == "Slider":
#     pass
