# 🌌 Sistema Solar Interativo em Pygame

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Portuguese](https://img.shields.io/badge/lang-pt--BR-yellow.svg)](README.md)

Uma simulação visual realista do Sistema Solar desenvolvida em Python com Pygame, representando os movimentos planetários com precisão orbital e detalhes visuais impressionantes.

![Sistema Solar](/images/solar_system.png)

## ✨ Características Principais

- **🪐 Representação Completa**: Todos os 8 planetas do sistema solar com órbitas circulares
- **🌞 Sol Centralizado**: Representação do Sol como corpo central gravitacional
- **💫 Velocidades Realistas**: Planetas mais distantes se movem mais lentamente (Leis de Kepler)
- **🪷 Anéis de Saturno**: Representação detalhada dos característicos anéis de Saturno
- **📝 Identificação Visual**: Nomes dos planetas exibidos para fácil reconhecimento
- **🎯 Órbitas Visíveis**: Trajetórias orbitais representadas por círculos cinza
- **⚡ Performance Otimizada**: Animação suave a 60 FPS

## 🚀 Instalação Rápida

### Pré-requisitos
- Python 3.8 ou superior
- Biblioteca Pygame

### Instalação das Dependências
```bash
# Instalar pygame
pip install pygame

# Ou usando pip3 se necessário
pip3 install pygame
```

### Execução do Projeto
```bash
# Clonar ou baixar o arquivo e executar
python sistema_solar.py

# Alternativamente, tornar o arquivo executável
chmod +x sistema_solar.py
./sistema_solar.py
```

## 🎮 Como Utilizar

Execute o script e observe a simulação em tempo real:

```bash
python sistema_solar.py
```

### Controles da Simulação
- **🖱️ Fechar**: Clique no 'X' da janela ou pressione `ESC`
- **⏸️ Pausar**: Feche a janela para interromper a simulação
- **🔍 Observar**: A simulação roda automaticamente - apenas observe e aprenda!

## ⚙️ Personalização Avançada

O código é altamente customizável. Edite os parâmetros diretamente no script:

### Configurações de Tela
```python
WIDTH, HEIGHT = 1200, 800  # Tamanho da janela
```

### Cores dos Corpos Celestes
```python
YELLOW = (255, 255, 0)     # Sol
GRAY = (150, 150, 150)     # Mercúrio
WHITE = (255, 255, 255)    # Vênus
BLUE = (100, 149, 237)     # Terra
RED = (188, 39, 50)        # Marte
BROWN = (165, 42, 42)      # Júpiter
ORANGE = (255, 165, 0)     # Saturno
CYAN = (0, 255, 255)       # Urano
LIGHT_BLUE = (173, 216, 230) # Netuno
```

### Parâmetros dos Planetas
Modifique a lista `planets` para ajustar:

```python
Planet("Nome", cor, raio, distância, velocidade, tem_anéis)
```

**Parâmetros:**
- `nome`: Nome do planeta (string)
- `cor`: Cor RGB do planeta
- `raio`: Tamanho visual em pixels
- `distância`: Raio orbital do Sol
- `velocidade`: Velocidade angular de rotação
- `tem_anéis`: Booleano para planetas com anéis

## 🏗️ Arquitetura do Código

### Classe `Planet`
A classe principal que gerencia cada corpo celeste:

```python
class Planet:
    def __init__(self, name, color, radius, distance, speed, has_rings=False):
        # Inicialização das propriedades
        self.name = name
        self.color = color
        self.radius = radius
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.has_rings = has_rings

    def update(self):
        # Atualiza a posição orbital
        self.angle += self.speed

    def draw(self, surface):
        # Renderiza planeta, órbita, anéis e nome
```

### Fluxo Principal
1. **Inicialização** → Configura Pygame e cria objetos Planet
2. **Loop Principal** → Processa eventos e atualiza frame a frame
3. **Renderização** → Desenha Sol, órbitas e planetas
4. **Atualização** → Calcula novas posições orbitais

## 🔬 Propriedades dos Planetas na Simulação

| Planeta  | Raio | Distância | Velocidade | Cor        | Anéis |
| -------- | ---- | --------- | ---------- | ---------- | ----- |
| Mercúrio | 5px  | 80px      | 0.04       | Cinza      | ❌     |
| Vênus    | 8px  | 120px     | 0.015      | Branco     | ❌     |
| Terra    | 10px | 180px     | 0.01       | Azul       | ❌     |
| Marte    | 7px  | 240px     | 0.008      | Vermelho   | ❌     |
| Júpiter  | 20px | 320px     | 0.004      | Marrom     | ❌     |
| Saturno  | 18px | 400px     | 0.002      | Laranja    | ✅     |
| Urano    | 12px | 480px     | 0.001      | Ciano      | ❌     |
| Netuno   | 12px | 560px     | 0.0007     | Azul Claro | ❌     |

## 🎯 Aplicações Educacionais

Este projeto é ideal para:

- **👨‍🎓 Estudantes de Astronomia**: Compreender movimentos planetários
- **👨‍🏫 Professores**: Demonstrar órbitas e velocidades angulares
- **💻 Programadores Iniciantes**: Aprender Pygame e animações
- **🔬 Entusiastas do Espaço**: Visualizar nosso sistema solar

## 🚀 Melhorias Futuras

- [ ] Adicionar luas para planetas selecionados
- [ ] Implementar órbitas elípticas realistas
- [ ] Adicionar controle de velocidade de simulação
- [ ] Incluir informações detalhadas sobre cada planeta
- [ ] Adicionar modo tela cheia e diferentes resoluções
- [ ] Implementar trilhas orbitais persistentes

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes completos.

## 🐛 Reportar Problemas

Encontrou um bug ou tem uma sugestão? [Abra uma issue](https://github.com/seu-usuario/sistema-solar/issues) no repositório.

## 👨‍💻 Autor

**Edius Ferreira**
📧 Email: [ediusferreira@gmail.com](mailto:ediusferreira@gmail.com)
🔗 GitHub: [@edius1987](https://github.com/edius1987)
📜 Licença: MIT

---

## 🌟 Destaques Técnicos

- **🔄 Animação Suave**: Frame rate constante de 60 FPS
- **🎨 Cores Cientificamente Inspiradas**: Baseadas em imagens reais dos planetas
- **📐 Geometria Orbital**: Uso de funções trigonométricas para movimentos circulares
- **⚡ Código Eficiente**: Classe reutilizável para todos os planetas

---

**⭐️ Se este projeto foi útil para você, considere dar uma estrela no repositório!**

---

*Nota: Esta é uma representação visual simplificada para fins educacionais. As escalas de tamanho e distância não são proporcionais à realidade.*
