#include "cursorhandler.h"
#include <QCursor>

CursorHandler::CursorHandler(QObject *parent) : QObject(parent) {}

QPoint CursorHandler::cursor_position() {
    return QCursor::pos();
}