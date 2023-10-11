import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 200, // Количество виртуальных пользователей (VUs)
  duration: '1s', // Продолжительность теста
};

export default function () {
  let url = 'http://0.0.0.0:8000/gpt?prompt=%D0%9D%D0%B0%D0%BF%D0%B8%D1%88%D0%B8%20%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D1%83%D1%8E%20%D1%88%D1%83%D1%82%D0%BA%D1%83%20%D0%BF%D1%80%D0%BE%20%D1%82%D0%B5%D1%89%D1%83';

  // Заголовки запроса
  let headers = {
    'accept': 'application/json',
    'x-api-key': 'qwe',
  };

  // Выполняем GET-запрос
  let res = http.get(url, { headers: headers });

  // Проверяем, что статус-код ответа равен 200 (OK)
  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  // Можно добавить дополнительные проверки, например, на содержимое ответа, если необходимо
  let randomSleep = Math.random() * 3;
  sleep(randomSleep);
}
