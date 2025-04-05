#pragma once

#include <QObject>
#include <qtmetamacros.h>

#ifdef Q_OS_WIN

#include <Windows.h>

class KeyListener : public QObject {
    Q_OBJECT
public:
    explicit KeyListener(QObject *parent = nullptr);
    ~KeyListener();

    static LRESULT CALLBACK keyboard_callback(int n_code, WPARAM w_param, LPARAM l_param);

private:
    static HHOOK keyboard_hook;

signals:
    void key_pressed(int key);
};

#endif // Q_OS_WIN