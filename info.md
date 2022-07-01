# СамараЛан для Home Assistant
 [![Лицензия](https://img.shields.io/badge/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![hacs_badge](https://img.shields.io/badge/HACS-Default-green.svg)](https://github.com/custom-components/hacs)

Данная интеграция предоставляет возможность системе HomeAssistant опрашивать сайт СамараЛан.

## Установка

### Посредством HACS
1. Откройте HACS (через `Extensions` в боковой панели)
1. Добавьте новый произвольный репозиторий:
   1. Выберите `Integration` (`Интеграция`) в качестве типа репозитория
   1. Введите ссылку на репозиторий: `https://github.com/ErilovNikita/hass-samaralan`
   1. Нажмите кнопку `Add` (`Добавить`)
   1. Дождитесь добавления репозитория (занимает до 10 секунд)
   1. Теперь вы должны видеть доступную интеграцию `SamaraLan (СамараЛан)` в списке новых интеграций.
1. Нажмите кнопку `Install` чтобы увидеть доступные версии
1. Установите последнюю версию нажатием кнопки `Install`
1. Перезапустите Home Assistant

_Примечание:_ Не рекомендуется устанавливать ветку `dev`. Она используется исключительно для разработки. 

### Вручную
Клонируйте репозиторий во временный каталог, затем создайте каталог `custom_components` внутри папки конфигурации
вашего Home Assistant (если она еще не существует). Затем переместите папку `samaralan` из папки `custom_components` 
репозитория в папку `custom_components` внутри папки конфигурации Home Assistant.
Пример (при условии, что конфигурация Home Assistant доступна по адресу `/mnt/homeassistant/config`) для Unix-систем:
```
git clone https://github.com/ErilovNikita/hass-samaralan.git
mkdir -p /config/custom_components
mv hass-samaralan/custom_components/samaralan /config/custom_components
```

## Конфигурация
### Через интерфейс Home Assistant

[![​Open your Home Assistant instance and start setting up a new integration.​](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=samaralan)

1. Откройте `Настройки` -> `Интеграции`
1. Нажмите внизу справа страницы кнопку с плюсом
1. Введите в поле поиска `samaralan` или `СамараЛан`
   1. Если по какой-то причине интеграция не была найдена, убедитесь, что HomeAssistant был перезапущен после установки интеграции.
1. Выберите первый результат из списка
1. Нажмите кнопку `Продолжить`
1. Через несколько секунд начнётся обновление; проверяйте список ваших объектов на наличие
   объектов, чьи названия начинаются на `smrlan`.
