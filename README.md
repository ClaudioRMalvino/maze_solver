# Maze Solver

A Python-based application that generates and solves mazes using depth-first search algorithms. The program creates random mazes and visually demonstrates the solving process in real-time.

##  Features

- **Random Maze Generation**: Creates unique mazes using a depth-first recursive backtracking algorithm
- **Interactive Visualization**: Real-time visualization of both maze generation and solving process
- **Customizable Dimensions**: Supports custom maze sizes with adjustable row and column counts
- **Animated Solution Path**: Shows the path-finding process with color-coded trails (red for current path, gray for backtracking)
- **Error Handling**: Robust handling of unsolvable maze configurations

##  Technologies Used

- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework for visualization
- **Object-Oriented Programming**: Modular design with separate classes for cells, maze, and window management

##  Architecture

The project is structured into several key components:

### Main Components
1. `main.py`: Entry point of the application
2. `maze.py`: Core maze generation and solving logic
3. `cells.py`: Cell object definition and drawing methods
4. `window.py`: Window management and canvas setup
5. `drawing.py`: Utility classes for drawing lines and points

### Key Classes

#### Cell Class
- Manages individual cell properties (walls, visited state)
- Handles drawing of cell walls and move animations
- Maintains cell position and dimensions

#### Maze Class
- Implements maze generation algorithm
- Contains solving logic using depth-first search
- Manages the grid of cells
- Handles entrance and exit creation

#### Window Class
- Creates and manages the Tkinter window
- Provides canvas for drawing
- Handles window updates and animations

##  How It Works

### Maze Generation
1. Creates a grid of cells with all walls intact
2. Uses recursive backtracking to:
   - Mark current cell as visited
   - Choose random unvisited neighbor
   - Remove walls between current cell and chosen neighbor
   - Recursively visit the next cell
3. Creates entrance and exit points

### Solving Algorithm
1. Uses depth-first search to find path from entrance to exit
2. Visualizes the search process:
   - Red lines show current path
   - Gray lines show backtracking
3. Continues until exit is found or all possibilities are exhausted

##  Performance Considerations

- Custom recursion limit handling for large mazes
- Optimized drawing operations with animation delays
- Efficient memory usage through object reuse

## Implementation Details

### Visualization Features
- Real-time cell drawing
- Wall removal animation
- Path-finding visualization
- Solution status display

## 🔧 Future Improvements

- Additional maze generation algorithms
- Multiple solving algorithms (A*, Dijkstra's)
- Save/load maze functionality
- Difficulty levels
- Performance optimizations for larger mazes

## 📈 Technical Highlights

- **Algorithm Efficiency**: O(N*M) time complexity for both generation and solving
- **Memory Usage**: O(N*M) space complexity where N and M are maze dimensions
- **Code Organization**: Clear separation of concerns between classes
- **Error Handling**: Robust handling of edge cases and invalid configurations

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- Object-oriented design principles
- Algorithm implementation
- GUI programming
- Data structures
- Recursive problem-solving
- Visual animation techniques


