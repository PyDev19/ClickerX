#pragma once

#include <QObject>
#include <QPoint>
#include <qtmetamacros.h>

class CursorHandler : public QObject {
    Q_OBJECT
public:
    explicit CursorHandler(QObject *parent = nullptr);

    Q_INVOKABLE QPoint cursor_position();
};