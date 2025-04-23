오늘은 java 프로그래밍 (캡슐화, 상속, 다형성, 추상클래스, 인터페이스)를 학습하는걸 목표로 

Spring tool Suite (sts) : spring 개발할때 사용자 최적화 한 tool 
자바는 jdk로 개발 하고 jre로 실행한다
spring starter project - Boot
static web project - Html,Css
Dynamic Web project - Servlet / jsp
java project - java 

java는 객체지향 언어 OOP(Object-Oriented Programming)
캡슐화
![image](https://github.com/user-attachments/assets/c027c61e-c51f-46ab-a2eb-4818b213ddf3)

-는 private / +는 publish
| 구분           | 규칙                                                                                                                             | 예시                                 | 추가 설명                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------ |
| **클래스 (Class)** | - 명사로 시작합니다. <br> - 각 단어의 첫 글자는 대문자로 표기합니다. (파스칼 케이스 / Upper Camel Case)                                  | `Customer`, `ProductService`         | 엔티티, 서비스 등의 주요 객체             |
| **인스턴스 변수 (Instance Variable)** | - 명사로 시작합니다. <br> - 첫 단어는 소문자로 시작하고, 이어지는 각 단어의 첫 글자는 대문자로 표기합니다. (카멜 케이스 / Lower Camel Case) | `customerName`, `orderQuantity`      | 클래스 내부의 속성                         |
| **메서드 (Method)** | - 동사로 시작합니다. <br> - 첫 단어는 소문자로 시작하고, 이어지는 각 단어의 첫 글자는 대문자로 표기합니다. (카멜 케이스 / Lower Camel Case)     | `calculateTotal()`, `updateStatus()` | 객체의 행위 또는 기능                     |
| **Getter 메서드** | - 일반적으로 `get`으로 시작하고, 뒤에 오는 프로퍼티 이름의 첫 글자는 대문자로 표기합니다. <br> - `boolean` 타입의 프로퍼티는 `is`로 시작할 수도 있습니다. | `getName()`, `getAge()`, `isActive()` | 속성 값을 읽어오는 메서드                   |
| **Setter 메서드** | - `set`으로 시작하고, 뒤에 오는 프로퍼티 이름의 첫 글자는 대문자로 표기합니다. <br> - 파라미터는 해당 프로퍼티와 동일한 타입과 이름을 사용합니다.                               | `setName(String name)`, `setPrice(double price)` | 속성 값을 설정하는 메서드                   |
| **상수 (Constant)** | - 모든 글자를 대문자로 표기하고, 단어 사이는 밑줄 (`_`)로 구분합니다. <br> - `static final`로 선언합니다.                                  | `MAX_SIZE`, `USER_AGENT`   | 변하지 않는 값                             |

