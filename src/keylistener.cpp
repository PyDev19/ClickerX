#include "keylistener.h"
#include <QDebug>
#include <QGuiApplication>

#ifdef Q_OS_WIN

HHOOK KeyListener::keyboard_hook = nullptr;

KeyListener::KeyListener(QObject *parent) : QObject(parent) {
    keyboard_hook = SetWindowsHookEx(WH_KEYBOARD_LL, keyboard_callback, GetModuleHandle(nullptr), 0);

    if (!keyboard_hook) {
        qDebug() << "Failed to install hook!";
    } else {
        qDebug() << "Global keyboard hook installed.";
    }

    setParent(qApp);
}

KeyListener::~KeyListener() {
    if (keyboard_hook) {
        UnhookWindowsHookEx(keyboard_hook);
    }
}

LRESULT CALLBACK KeyListener::keyboard_callback(int n_code, WPARAM w_param, LPARAM l_param) {
    if (!qApp || n_code < 0) return CallNextHookEx(keyboard_hook, n_code, w_param, l_param);

    auto *self = qApp->findChild<KeyListener *>();
    if (!self) return CallNextHookEx(keyboard_hook, n_code, w_param, l_param);

    KBDLLHOOKSTRUCT *keyboard_struct = reinterpret_cast<KBDLLHOOKSTRUCT *>(l_param);

    if (w_param == WM_KEYDOWN) {
        emit self->key_pressed(keyboard_struct->vkCode);
    }

    return CallNextHookEx(keyboard_hook, n_code, w_param, l_param);
}

#endif