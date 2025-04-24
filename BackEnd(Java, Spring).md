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






프레임워크의 정의
비기능적 요구사항(성능, 보안, 확장성, 안정성등)을 만족하는 구조와 구현된 기능을 안정적으로 실행하도록 제어해주는 잘 만들어진 구조의 라이브러리 덩어리

프레임워크는 애플리케이션들의 최소한 공통점을 찾아 하부 구조를 제공함으로서 개발자들로 하여금 시스템의 하부 구조를 구현하는데 들어가는 노력을 절감하게 해줌 

프레임 워크를 왜쓸까

디자인패턴과 프레임워크의 관련성
디자인 패턴은 프레임워크의 핵심적인 특징이고, 

프레임워크(Framework)와 라이브러리(Library)의 차이점
호출 흐름의 주도권을 누가 가지고 있느냐?
Library - 라이브러리를 사용하는 개발자
Framework - 개발자의 제어권을 가져와서 **프레임워크가 대신 객체생**성하고, 객체의 라이프사이클관리를 해준다.
IoC(Inversion of Control) - 제어의 역전 


스프링프레임워크는 Programming와 Configuration 모데을 제공한다.
Configuration 모델이 필요한 이유
:프레임워크가 개발자 대신 객체를 관리하므로 프레임워크에게 클래스에 대한 정보(패키지명,클래스명,연관관계)를 제공해야 하기 때문이다.
:XML형태의 설정 파일을 작성, @Component, @Autowired 와 같은 어노테이션을 사용 

프레임워크가 제어권을 가져간 이유?
:infrastructural support를 하기 위해서
예를들어 스프링이 관리하는 객체인 Spring Bean은 Default Scope가 모두 Singleton Pattern(싱글톤 패턴)을 적용해서 객체를 대신 생성해 준다.

IOC

