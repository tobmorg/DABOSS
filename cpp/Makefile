# =========================
# Compiler and flags
# =========================
COMPILER = g++
FLAGS = -fopenmp -ftree-vectorize -ffast-math -O3 -flto -march=native -Iinclude


# ========================= 
# Targets
# =========================
TARGET = daboss

# =========================
# Directories
# =========================
SRC_DIR = src
BUILD_DIR = build

# =========================
# Source and object files
# =========================
SRCS = \
	$(SRC_DIR)/run_debiasing.cpp \
	$(SRC_DIR)/debiasing.cpp \
	$(SRC_DIR)/calc_obs_time.cpp \
	$(SRC_DIR)/calc_obs_time_vitense.cpp \
	$(SRC_DIR)/generate_orbit_points.cpp

OBJS = \
	$(BUILD_DIR)/run_debiasing.o \
	$(BUILD_DIR)/debiasing.o \
	$(BUILD_DIR)/calc_obs_time.o \
	$(BUILD_DIR)/calc_obs_time_vitense.o \
	$(BUILD_DIR)/generate_orbit_points.o

# =========================
# Default target
# =========================
all: $(TARGET)

# =========================
# Link step
# =========================
$(TARGET): $(OBJS)
	$(COMPILER) $(FLAGS) -o $@ $^

# =========================
# Compile step
# =========================
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(BUILD_DIR)
	$(COMPILER) $(FLAGS) -c $< -o $@

# =========================
# Clean
# =========================
clean:
	rm -rf $(BUILD_DIR) $(TARGET)

.PHONY: all clean
