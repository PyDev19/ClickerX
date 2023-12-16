#include <QQmlApplicationEngine>
#include <QGuiApplication>
#include <QQmlContext>
#include <QIcon>
#include <ui.hpp>

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
	app.setWindowIcon(QIcon(":/icons/icon.ico"));

    QQmlApplicationEngine engine;

    UI ui(engine);
    engine.rootContext()->setContextProperty("ui", &ui);

    engine.load(QUrl("qrc:qml/main.qml"));

    QList<QObject*> root_objects = engine.rootObjects();
    if (root_objects.isEmpty()) return -1;

    QObject* root_object = root_objects.first();

	if (ui.setup_ui(root_object) == -1) {
		return -1;
	}

    return app.exec();
}
