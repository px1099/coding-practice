package golang

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

//lint:ignore U1000 (example)
func scan_int_slice() []int {
    line := scan_line()
	var int_slice []int
	for _, field := range strings.Fields(line) {
		num, err := strconv.Atoi(field)
		if err != nil {
			log.Fatal(err)
		}
		int_slice = append(int_slice, num)
	}
	return int_slice
}

//lint:ignore U1000 (example)
// Scan a line as string
func scan_line() string {
	scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
	line := scanner.Text()
	return line
}

//lint:ignore U1000 (example)
// Scan lines as slice of string until empty line
func scan_lines() []string {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for {
		scanner.Scan()
		line := scanner.Text()
		if len(line) == 0 {
			break
		}
		lines = append(lines, line)
	}
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
	return lines
}

//lint:ignore U1000 (example)
// Scan all lines as slice of string
func scan_all_lines() []string {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
	return lines
}

//lint:ignore U1000 (example)
// Scan a line as string (including newline)
func scan_line_include_newline() string {
	reader := bufio.NewReader(os.Stdin)
    line, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	return line
}

//lint:ignore U1000 (example)
// Scan lines as slice of string until empty line (including newline)
func scan_lines_include_newline() []string {
	reader := bufio.NewReader(os.Stdin)
	var lines []string
	for {
        line, err := reader.ReadString('\n')
        if err != nil {
            log.Fatal(err)
        }
        if len(strings.TrimSpace(line)) == 0 {
            break
        }
        lines = append(lines, line)
    }
	return lines
}
